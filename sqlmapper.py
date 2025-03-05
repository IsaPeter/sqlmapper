import os
from argparse import ArgumentParser 
from burp_reader import BurpRequests


def parse_arguments():
    parser = ArgumentParser()
    command_parser = parser.add_argument_group("Command Creation")
    command_parser.add_argument("--requests", dest="requests", metavar="", help="Set the requests path")
    command_parser.add_argument("--extra-args", dest="extra_args", metavar="", help="Append extra arguments to the final command")
    command_parser.add_argument("--result-out", dest="result_out", metavar="", help="Result files output path")

    exp_parser = parser.add_argument_group("Request Exporting")
    exp_parser.add_argument("--export-requests", dest="export_requests", metavar="", help="Exporting requests from a burp file")
    exp_parser.add_argument("--export-out", dest="export_out", metavar = "", help="Exported content output folder")
    
    return parser.parse_args()


def write_request(data,path):
    with open(path, "w") as file:
        file.write(data)



def main():
    args = parse_arguments()

    if args.requests:
        extra_args = args.extra_args if args.extra_args else ""
        result_out_path = args.result_out if args.result_out else ""

        requests = os.listdir(args.requests)
        commands = []
        template = f"sqlmap -r PATH"
        for req in requests:
            rqpath = os.path.join(args.requests,req)
            final_file_name = f"sqlmap_result_{req}.txt"
            print(f"sqlmap -r {rqpath} --batch --tamper between --hostname --current-user {extra_args} | tee {os.path.join(result_out_path, final_file_name)}")

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
