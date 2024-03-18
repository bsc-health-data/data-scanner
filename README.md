# data-scanner

- prepare the environment
  
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas openpyxl PyQt5 pyinstaller

```

```
pyinstaller --onefile --windowed scanner.py

```
In case of recursion errors add 

```
import sys
sys.setrecursionlimit(5000)
```
to `scanner.spec` and run 

```
pyinstaller scanner.spec

```

Finally, execute ./dist/scanner
