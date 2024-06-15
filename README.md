# Evil PyTorch Model (.pth RCE Exploit)

A Python script demonstrating a potential security vulnerability in PyTorch's model serialization using `torch.save`.

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [Example](#example)
- [Security Considerations](#security-considerations)
- [License](#license)

## Overview

This script creates an "evil" PyTorch model (`EvilModel`) that showcases a security vulnerability related to PyTorch's model serialization using `torch.save`. The `EvilModel` class overrides PyTorch's `__reduce__` method to execute arbitrary commands passed as arguments during deserialization.

## Usage

1. **Clone the Repository:**

   ```bash
   $ git clone https://github.com/duck-sec/pytorch-evil-pth.git
   $ cd pytorch-evil-pth.git
   ```

2. **Run the Script:**

   Use Python to execute the script, providing a command to execute as an argument. Ensure you have PyTorch installed.

   ```bash
   $ python evil_pth.py '<command>'
   ```

   Replace `<command>` with any shell command you want to execute when the malicious model (`evil_model.pth`) is loaded.

## Example

```bash
$ python evil_pth.py 'touch /tmp/gotya'
Evil model saved as 'evil_model.pth'
```


