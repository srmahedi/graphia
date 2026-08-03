import cv2
import sys
import os

try:
    get_image = sys.argv[1]
except:
    if getattr(sys, 'frozen', False):
        print("usage: graphia <path/of/image>")
        sys.exit(1)
    else:
        if os.name == 'nt':
            print("usage: python main.py <path/of/image>")
            sys.exit(1)
        else:
            print("usage: python3 main.py <path/of/image>")
            sys.exit(1)

output = os.path.join(os.path.dirname(get_image), "graphia")

if not os.path.exists(output):
    try:
        os.mkdir(os.path.join(output))
    except Exception as e:
        print(e)
        sys.exit(1)

try:
    img = cv2.imread(get_image, cv2.IMREAD_UNCHANGED)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    get_name = os.path.basename(get_image)
    file_name, file_ext = os.path.splitext(get_name)
    output_file = os.path.join(output, f"{file_name}-gray{file_ext}")

    cv2.imwrite(output_file, gray)

    print(f"Output: {output_file}")
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(1)