def create_dataset():
    # Define the dataset output file
    output_path = "/Users/zahid/Downloads/shared/privacy and data mining/ml/dataset/dataset.tsv"
    custom_separator = "|"  # Custom separator

    # Open the output file for writing
    with open(output_path, 'w') as f:
        # Process malware traces
        for i in range(1, 11):
            mal_path = f'/Users/zahid/Downloads/shared/privacy and data mining/ml/dataset/mal/{i}.trace'
            try:
                with open(mal_path, 'r') as mal:
                    for line in mal:
                        # Write the trace and label (1 for malware)
                        f.write(f"{line.strip()}{custom_separator}1\n")
            except FileNotFoundError:
                print(f"File not found: {mal_path}")

        # Process safe app traces
        for i in range(1, 11):
            safe_path = f'/Users/zahid/Downloads/shared/privacy and data mining/ml/dataset/safe/{i}.trace'
            try:
                with open(safe_path, 'r') as pure:
                    for line in pure:
                        # Write the trace and label (0 for safe apps)
                        f.write(f"{line.strip()}{custom_separator}0\n")
            except FileNotFoundError:
                print(f"File not found: {safe_path}")


if __name__ == '__main__':
    create_dataset()
    print("Dataset creation completed.")

