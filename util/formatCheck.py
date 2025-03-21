# Basic parameter and quality check of icon files

import os
import re

def check_svg_compliance(folder_path):
    svg_files = [f for f in os.listdir(folder_path) if f.endswith('.svg')]
    compliance_report = {}
    
    summary_compliance = True

    for file in svg_files:
        file_path = os.path.join(folder_path, file)
        file_size = os.path.getsize(file_path)  # Get file size in bytes

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for required viewBox attribute
        viewbox_match = re.search(r'viewBox="0 0 32 32"', content)

        # Check for required fill color
        fill_match = re.search(r'fill="{fillColor}"', content)

        # Check for newline characters
        has_newline = "\n" in content

        # Check if file size is within limits
        within_size_limit = file_size <= 2500

        # Determine compliance
        is_compliant = bool(viewbox_match and fill_match and not has_newline and within_size_limit)

        if not is_compliant:
            summary_compliance = False
        
        compliance_report[file] = {
            "viewBox": bool(viewbox_match),
            "fill": bool(fill_match),
            "newline": has_newline,
            "size": file_size,
            "within_size_limit": within_size_limit,
            "compliant": is_compliant
        }

    # Print report
    for file, status in compliance_report.items():
        print(f"File: {file}")
        print(f"  - ViewBox correct: {status['viewBox']}")
        print(f"  - Fill correct: {status['fill']}")
        print(f"  - Contains newline: {status['newline']}")
        print(f"  - File size: {status['size']} bytes (<= 1500: {status['within_size_limit']})")
        print(f"  - Compliant: {'✅ Yes' if status['compliant'] else '❌ No'}")
        print("-" * 40)
    
    print("Summary:")
    print(f"  - Summary of Compliance: {'✅ Yes' if summary_compliance else '❌ No'}")
    print("-" * 40)

    

# Usage
folder_path = "../icons"  # Change to your folder path
check_svg_compliance(folder_path)

