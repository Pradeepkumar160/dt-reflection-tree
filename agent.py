#!/usr/bin/env python3
"""
Daily Reflection Tree — CLI Agent
Loads reflection-tree.json and walks it deterministically. Zero LLM calls.
Usage: python agent.py [path/to/reflection-tree.json]
"""
import json, sys, os, time, textwrap
from pathlib import Path

def load_tree(path):
    with open(path) as f:
        nodes = json.load(f)
    tree = {n["id"]: n for n in nodes}
    children = {n["id"]: [] for n in nodes}
    for n in nodes:
        if n.get("parentId") and n["parentId"] in children:
            children[n["parentId"]].append(n["id"])
    return tree, children

def slow_print(text, delay=0.016, width=64):
    wrapped = textwrap.fill(text, width=width)
    for ch in wrapped:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def interpolate(text, state):
    import re
    def repl(m):
        parts = m.group(1).split(".")
        return state["answers"].get(parts[0], f"[{m.group(1)}]")
    return re.sub(r"\{([^}]+)\}", repl, text)

def apply_signal(signal, state):
    if not signal: return
    axis, pole = signal.split(":")
    if axis in state: state[axis][pole] = state[axis].get(pole, 0) + 1

def resolve_decision(node, state):
    parent = node.get("parentId", "")
    last = state["answers"].get(parent, "")
    for rule in node.get("options", []):
        if ":" not in rule: continue
        cond, target = rule.split(":", 1)
        if cond.startswith("answer="):
            if last in cond[7:].split("|"): return target
    if node["options"] and ":" in node["options"][0]:
        return node["options"][0].split(":", 1)[1]
    return None

def find_next(node, children):
    if node.get("target"): return node["target"]
    kids = children.get(node["id"], [])
    return kids[0] if kids else None

def dominant(axis_state):
    if not axis_state: return "unclear"
    return max(axis_state, key=axis_state.get)

def run(tree_path):
    tree, children = load_tree(tree_path)
    state = {"answers": {}, "axis1": {}, "axis2": {}, "axis3": {}}
    W = 64

    print("\n" + "━" * W)
    print("  🌙  DAILY REFLECTION — DeepThought")
    print("━" * W + "\n")
    time.sleep(0.5)

    current_id = "START"
    q_num = 0

    while current_id:
        node = tree.get(current_id)
        if not node: print(f"[Error: node {current_id} not found]"); break

        t = node["type"]
        text = interpolate(node.get("text", ""), state)
        apply_signal(node.get("signal", ""), state)

        if t == "start":
            slow_print(text)
            time.sleep(1)
            current_id = find_next(node, children)

        elif t == "question":
            q_num += 1
            opts = node["options"]
            print(f"\n  [{q_num}]  ", end="")
            slow_print(text, delay=0.014)
            print()
            for i, o in enumerate(opts, 1):
                print(f"  {i}.  {o}")
            print()
            while True:
                try:
                    ch = input("  Your choice (1–4): ").strip()
                    idx = int(ch) - 1
                    if 0 <= idx < len(opts):
                        state["answers"][node["id"]] = opts[idx]
                        print(f"\n  ✓  {opts[idx]}\n")
                        time.sleep(0.3)
                        break
                    else: print(f"  Enter 1–{len(opts)}.")
                except (ValueError, KeyboardInterrupt):
                    print(f"  Enter 1–{len(opts)}.")
            current_id = find_next(node, children)

        elif t == "decision":
            current_id = resolve_decision(node, state)

        elif t == "reflection":
            print("\n  ┌" + "─" * (W - 4) + "┐")
            print("  │  Reflection" + " " * (W - 17) + "│")
            print("  │" + " " * (W - 4) + "│")
            wrapped = textwrap.wrap(text, width=W - 8)
            for line in wrapped:
                print(f"  │  {line:<{W-8}}  │")
            print("  │" + " " * (W - 4) + "│")
            print("  └" + "─" * (W - 4) + "┘")
            input("\n  [ Enter to continue ]")
            current_id = node.get("target") or find_next(node, children)

        elif t == "bridge":
            print(f"\n  ─── {text}\n")
            time.sleep(1.5)
            current_id = node.get("target") or find_next(node, children)

        elif t == "summary":
            tpl = node.get("summaryTemplates", {})
            a1 = dominant(state["axis1"])
            a2 = dominant(state["axis2"])
            a3 = dominant(state["axis3"])
            print("\n" + "━" * W)
            print("  📋  TODAY'S REFLECTION SUMMARY")
            print("━" * W)
            print(f"\n  I   · Locus       →  {a1.upper()} — {tpl.get('axis1',{}).get(a1,'')}")
            print(f"  II  · Orientation →  {a2.upper()} — {tpl.get('axis2',{}).get(a2,'')}")
            print(f"  III · Radius      →  {a3.upper()} — {tpl.get('axis3',{}).get(a3,'')}")
            print("\n  Three honest answers. Sleep on it.")
            print("\n" + "━" * W)
            input("\n  [ Enter to finish ]")
            current_id = find_next(node, children)

        elif t == "end":
            print(f"\n  {text}")
            print("\n" + "━" * W + "\n")
            break

        else:
            current_id = find_next(node, children)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parent.parent / "tree" / "reflection-tree.json"
    if not os.path.exists(path):
        print(f"Tree not found: {path}\nUsage: python agent.py [path/to/reflection-tree.json]")
        sys.exit(1)
    try:
        run(path)
    except KeyboardInterrupt:
        print("\n\n  Session ended. See you tomorrow.\n")
