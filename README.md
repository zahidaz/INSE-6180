# Leveraging Large Language Models for Android Malware Classification Based On Method Tracing

## Project Overview
This project focuses on developing a framework for Android malware detection by leveraging method tracing information. It includes tools and scripts for dynamic instrumentation of Android applications, trace collection, preprocessing, and fine-tuning a BERT-based model for binary classification.

## Requirements

### Software Dependencies
Ensure the following software and tools are installed:
- **Linux** operating system with the `uv` package manager.
- Python 3.7 or higher.
- **Frida**: For dynamic instrumentation.
- **ADB**: Android Debug Bridge for device communication.

### Hardware Requirements
- Rooted Android emulator or physical device for testing.
- Sufficient system resources for training machine learning models (GPU recommended).

## Setup Instructions

### Step 1: Install Dependencies
Use the `uv` package manager to install system dependencies:
```bash
uv install
```

### Step 2: Prepare the Environment
1. **Ensure Rooted Emulator/Device**:
   Set up a rooted Android emulator or a rooted physical device.
2. **Enable ADB Connection**:
   Connect the device/emulator via ADB:
   ```bash
   adb devices
   ```
   Ensure the device is listed and accessible.

### Step 3: Data Collection
1. **Instrument Applications**:
   Use Frida to dynamically inject code for method tracing:
   ```bash
   frida -U -f <package_name> --codeshare fdciabdul/frida-multiple-bypass -l out/_agent.js
   ```
2. **Extract Trace Files**:
   Run the provided `trace_puller.sh` script:
   ```bash
   ./trace_puller.sh <package_name> /output_directory
   ```

### Step 4: Trace Cleaning and Merging
Clean and preprocess trace files:
```bash
python3 trace_cleaner.py /output_directory /output_directory/merged.trace
```

### Step 5: Model Training
1. Prepare the dataset in the format required by the script.
2. Train the model:
   ```bash
   python3 finetune.py
   ```