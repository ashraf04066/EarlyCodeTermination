import os
import re

def count_methods_with_asserts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    method_pattern = re.compile(r"(public)\s+(void|[\w<>]+)\s+(\w+)\s*\(", re.MULTILINE)
    count = 0
    method_matches = method_pattern.finditer(code)

    for match in method_matches:
        method_start = match.start()
        brace_count = 0
        method_end = -1

        for i, char in enumerate(code[method_start:]):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    method_end = method_start + i
                    break

        if method_end != -1:
            method_code = code[method_start:method_end]
            asserts = re.findall(r"collector[A-Za-z]*\(", method_code)
            if len(asserts) > 1:
                count += 1

    return count

def main():
    root_dir = 'E:/Projects/data mining/Solution/sample_file/test_files2'  # Update this path to the root directory containing your Java files
    total_count = 0

    for folder, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(folder, file)
                count = count_methods_with_asserts(file_path)
                total_count += count
                print(f"{file_path}: {count} methods")

    print(f"Total number of methods with more than one assert: {total_count}")

if __name__ == "__main__":
    main()
