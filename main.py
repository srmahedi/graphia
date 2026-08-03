import cv2
import sys
import os

try:
    get_image = sys.argv[1] # try to get the image file from cli argument
except:
    # show usage when using pyinstaller bundle
    if getattr(sys, 'frozen', False):
        print("usage: graphia <path/of/image>")
        sys.exit(1)
    else:
        if os.name == 'nt':
            # show usage when running as python script in windows
            print("usage: python main.py <path/of/image>")
            sys.exit(1)
        else:
            # show usage when running as python script in linux, macOS
            print("usage: python3 main.py <path/of/image>")
            sys.exit(1)

# output dir
output = os.path.join(os.path.dirname(get_image), "graphia")

# create the output dir if not already exists
if not os.path.exists(output):
    try:
        os.mkdir(os.path.join(output))
    except Exception as e:
        print(e)
        sys.exit(1)

try:
    # read the image
    img = cv2.imread(get_image, cv2.IMREAD_UNCHANGED)

    # convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # get file name and ext and output
    get_name = os.path.basename(get_image)
    file_name, file_ext = os.path.splitext(get_name)
    output_file = os.path.join(output, f"{file_name}-gray{file_ext}")

    # write the image
    cv2.imwrite(output_file, gray)

    print(f"Output: {output_file}")
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(1)