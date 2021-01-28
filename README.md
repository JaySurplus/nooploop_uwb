# **Nooploop LinkTrack UWB**

## **Overview**
Unofficial Nooploop LinkTrack UWB Devices Python API. It parses Nooploop LinkTrack UWB Protocols.
    
* Nooploop Homepage: [https://www.nooploop.com/](https://www.nooploop.com/)

## Supported Devices
| Product | Supported? | Protocols |
| :-----: | :--------: | :-------: |
| LinkTrack |  **NO**  |     -     |
| LinkTrack AOA | **Partial** | NLink_LinkTrack_AOA_Node_Frame0 |

## Installation

### System

**Ubuntu20.04** (Ubuntu18.04, Windows Should also work fine.)

### Prerequisites (If you want to build from source)

* Setuptools,
* Wheel
    
Install with one line.
    
```bash
(your terminal)$: pip install --upgrade pip setuptools wheel
```


### Dependencies

pyserial >= 3.5 (Tested with 3.5. Lower version should works fine.)

### Install
* **Build From Source**

1. Download Source Code.
2. Change directory to source code root.
3. Running Command in your terminal
```bash
$: python setup.py sdist bdist_wheel
```
4. Change directory to `(source code root)/dist`. Run
```bash
(source code root)$: pip install ./Nooploop_UWB-0.0.1-py3-none-any.whl
```
5. You are all set.

* **Install From Release**

1. Download `Nooploop_UWB-0.0.1-py3-none-any.whl`
2. Change directory to `(Your downloads directory)`. Run
```bash
(Your downloads directory)$: pip install ./Nooploop_UWB-0.0.1-py3-none-any.whl
```
3. You are all set.

### Run Example

1. Change directory to `(source code root)/examples`. Run
```bash
(source code root)$:python examples.py
```

