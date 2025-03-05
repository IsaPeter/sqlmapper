import os
from argparse import ArgumentParser 
from burp_reader import BurpRequests


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--requests", dest="requests", metavar="", help="Set the requests path")
    parser.add_argument("--export-requests", dest="export_requests", metavar="", help="Exporting requests from a burp file")
    parser.add_argument("--export-out", dest="export_out", metavar = "", help="Exported content output folder")
    parser.add_argument("--extra-args", dest="extra_args", metavar="", help="Append extra arguments to the final command")

    return parser.parse_args()


def write_request(data,path):
    with open(path, "w") as file:
        file.write(data)



def main():
    args = parse_arguments()

    if args.requests:
        extra_args = args.extra_args if args.extra_args else ""

        requests = os.listdir(args.requests)
        commands = []
        template = f"sqlmap -r PATH"
        for req in requests:
            rqpath = os.path.join(args.requests,req)
            print(f"sqlmap -r {rqpath} --batch --tamper between --hostname --current-user {extra_args} | tee sqlmap_result_{req}.txt")

    if args.export_requests:
        export_out = args.export_out if args.export_out else ""
        
        requests = BurpRequests(args.export_requests)
        cnt = 1
        for req,resp in requests.items:
            pth = os.path.join(export_out,"req"+str(cnt))
            write_request(req.raw_request, pth)
            cnt += 1



if __name__ == '__main__':
    main()
