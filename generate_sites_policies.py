#!/usr/bin/env python3
import sys
from bs4 import BeautifulSoup as bs
from colorama import Fore, Back, Style


if len(sys.argv) == 2 and sys.argv[1] == 'help':
    print(Fore.LIGHTCYAN_EX + "Usage:\npython generate_sites_policies.py arg1 arg2\n\n  - arg1: the type of policies you want in the website.\n  - arg2: the title of this policy, for naming the file and be the title of the html.\n\nPossible rules are:\n  - minlength: minimum length of the generated password\n  - maxlength: maximum length of the generated password\n  - required: the character classes that are mandatory\n  - allowed: the character classes that are allowed, yet, are not mandatory, i.e., they may or may not exist\n\nThe possible values for character classes are:\n  - lower: lowercase characters - 'a-z'\n  - upper: uppercase characters - 'A-Z'\n  - digit: digits - '0-9'\n  - special: special characters - currently, only '!@#$%^&*'\n------------------------------------------\n\nThe values should be in a JSON format, i.e., \"minlength:14;maxlength:25;required:upper;allowed:digit;\"\n\n")
    quit()

elif len(sys.argv) != 3:
    print(Fore.RED + 'Please provide passwordRules and a short description of these rules.')
    quit()


input_rule = sys.argv[1]
description = sys.argv[2]

base_website = "<!DOCTYPE html><html><head><script src=\"js/jquery.js\"></script><link rel=\"stylesheet\" type=\"text/css\" href=\"css/style.css\" />    <!------ Include the above in your HEAD tag ----------></head><body id=\"LoginForm\">    <div class=\"container\">        <h1 class=\"form-heading\">" + description + "</h1>        <div class=\"login-form\">            <form id=\"Login\" method=\"POST\" action=\"/submit\">                <div class=\"form-group\">                    <input type=\"email\" class=\"form-control\" name=\"email\" id=\"inputEmailHidden\" placeholder=\"Email Address\">                </div>                <div class=\"form-group\">                    <input type=\"password\" class=\"form-control\" name=\"password\" id=\"inputPasswordHidden\" placeholder=\"New Password\" passwordrules=" + \
    input_rule + ">                                   </div>                <div class=\"form-group\">                    <input type=\"password\" class=\"form-control\" name=\"password\" id=\"inputConfirmPasswordHidden\" placeholder=\"Confirm New Password\">                </div>                <button type=\"submit\" class=\"btn btn-primary\">Login</button>            </form>        </div>    </div>    </div>    </div>    </body></html>"

html_file = bs(base_website, features="html.parser").prettify()

description = description.replace(" ", "_")

server_string = "\n\napp.get('/" + description + "', function(req, res) {\n\tres.sendFile(path.join(__dirname + '/" + description + ".html'));\n});"
print(server_string)

description = description + ".html"

with open(description, 'w+') as f:
    f.write(html_file)

with open('server.js', 'a') as srv:
    srv.write(server_string)