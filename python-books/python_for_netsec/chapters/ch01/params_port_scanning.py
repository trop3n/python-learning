import argparse
if __name__ == "__main__":
    description = """ Use cases:
        +  Basic scan:
            -target 127.0.0.1
        +  Specific port:
            -target 127.0.0.1 - port 21
        +  Port list:
            -target 127.0.0.1 -port 21,22
        +  Only show open ports
            -target 127.0.0.1 --open True """
    parser = argparse.ArgumentParser(description='Port scanning', epilog=description,
    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-target", metavar='TARGET', dest="target", help="target to scan", required=True)
    parser.add_argument("-ports", dest="ports",
                        help="Please, specify the target port(s) separated by" \
                        "comma[80,8080 by default]")
    parser.add_argument('-v', dest='verbosity', default=0, action="count",
                        help="verbosity level: -v, -vv, -vvv.")
    parser.add_argument("--open", dest="only_open", action="store_true",
                        help="only display open ports", default=False)