#!/usr/bin/env python3
import json


def correct_order(meta_to_correct: list, namespace):
    filtered_list = [info for info in meta_to_correct if namespace in info["Name"]]
    number = 1
    for var in meta_to_correct:
        if var in filtered_list:
            var["Name"] = namespace + "::" + str(number)
            number += 1
    return meta_to_correct
        

def update(initial_meta: list, command: str, namespace: str, value, type=1):
    if command == "append":
        if isinstance(value, list):
            number = -1
            for val in value:
                new_info = {"Name": f"{namespace}::{number}", "Type": type, "Value": val}
                initial_meta.append(new_info)
                number -= 1
        else:
            new_info = {"Name": namespace, "Type": type, "Value": value}
            initial_meta.append(new_info)
    elif command == "delete":
        for initial_info in initial_meta:
            if namespace in initial_info.get("Name"):
                if isinstance(value, list):
                    for val in value:
                        if val == initial_info.get("Value"):
                            initial_meta.remove(initial_info)
                else:
                    if value == initial_info.get("Value"):
                        initial_meta.remove(initial_info)
    else:
        raise Exception(f"Command {command} is not available!")
    return correct_order(initial_meta, namespace)


def main(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    meta_new = update(meta, "append", "GTL::Build::Tags", ["DX13", "Uplay", "DLSS"], 1)
    new_meta = update(meta_new, "delete", "GTL::Build::Categories", "NODRM")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(new_meta, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main("example.json")
