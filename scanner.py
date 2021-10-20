#code untested

import de2120_barcode_scanner
import time

scanner = de2120_barcode_scanner.DE2120BarcodeScanner()
scan_buffer = ""

while True:
    scan_buffer = scanner.read_barcode()
    printf("\n Package authorized for: " str(scan_buffer))
    scan_buffer = ""
    printf("\n Crate unlocked.")
    try:
        exec(open("lock.py").read())
    except SystemExit:
            pass