Plug-'n-play server that helps me to test my development on password rules for password managers.

I created the script `generate_sites_policies.py` which generates a basic html website to test different password rules.

In order to generate these websites, simple run `python generate_sites_policies.py <arg1> <arg2>`.

`<arg1>` consists of the policy you want to test.
`<arg2>` the name of the file to be generated. The site will also have this title.

### The available rules are:

-   `minlength` - minimum length of the password
-   `maxlength`- maximum length of the password
-   `required`- the mandatory character classes to be included in the password
-   `allowed` - the allowed character classes that may or may not be included in the password

### The character classes are:

-   `upper` - Uppercase letters - `A-Z`
-   `lower` - Lowercase letters - `a-z`
-   `digit` - Digits - `0-9`
-   `special` - Special characters. Currently, only `!@#$%^&*` are allowed.

**NOTE** Use quotation marks - `"` around both arguments.

### Example usage

`python generate_sites_policies.py "minlength:25;maxlength:30;required:upper;allowed:digit; "example"`

This will generate the file example.html

To run the server, `npm i` and then `npm start` or `node server.js`

## Requirements

-   python3
-   node

The `requirements.txt` has the two libraries/classes I'm using extra of the default in python. You may or may not already have them.

---

## Disclaimer

This dummy server is based on the server and website developed by [Sean Oesch](https://userlab.utk.edu/sean-oesch). I merely use it to have a ready to go server on which to test my development.

All credits go to the original author, and I thank him for making available his code.

The original repo can be found [here](https://bitbucket.org/user-lab/oesch2020that/src/master/)
