# instagram-refiner

This repository is a tool that can analyze the data from instagram in order to
spot follower accounts that are not following back.

This is helpful if someone wants to refine its feed page to contain mostly closer friends 
(Since this method will spot influencers, corporate accounts and else, as they generally does not follow back.) 

## Installation


```
pip install git+https://github.com/thomashirtz/declutter-instagram#egg=declutter-instagram
```
You can now call the application using `instagram-refiner` or `ir`

<details><summary>Never used python nor github before ?</summary>

1. Install Python 3.7 or above (tutorial available online)
2. Install [pip](https://pip.pypa.io/en/stable/installation/) (Generally included with Python)
3. Run the command `pip install ...` above using your machine command prompt (Maybe you would need to launch the command prompt as administrator on Windows)

</details>

## How to use ?

After installing the library, you need to do the following steps:

### 1. Request your instagram data

Via the browser :   
Settings => Privacy and Security => Data Download => Request Download => JSON => Next => Request Download  
Wait that the link is available (in your email inbox)  

Via the App :
Settings => Search "Download" => Download Information => Request Download 

[Guide](https://help.instagram.com/181231772500920) on the official instagram website.

### 2. Download your data

Download the instagram information via the email obtained in your email inbox.

### 3. Use the tool

Using the command prompt, run the command:
```
instagram-refiner path_to_the_file
```

It will output the list of the account you follow and are not following back:
```

```

## Buy me a coffee ツ

If this repository helped you or you if you like this project, feel free to support me!  

<a href="https://www.paypal.com/donate/?hosted_button_id=2KQR9V6PRSBPC">
  <img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" alt="Donate with PayPal" width="180" />
</a>

## License

     Copyright 2022 Thomas Hirtz

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.