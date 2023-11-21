---
# Metadata
date: "2023-10-19"
author: "RH"
documentType: "howToConfigure"
---

# Configure Vim IDE

## Introduction

### Document_Overview

This document covers the requirements and installation process of VIM and `LazyVim`. `LazyVim` is the IDE solution we're going with for this project due to its versatile functionalities and unparalleled performance/scalability potential.
This document, along with other documents with the configuration directory are designed to ensure that you complete the setup quickly and accurately, ideally from the first go.
It's no secret that installing VIM as well as its learning curve are considered somewhat complex, however, it's worth noting that `lvim` (`LazyVim`), is a game changer if you factor it into your workflow.

This document consists of 6 parts as follows:

- **1.Introduction:** The current section. Contains key information on the document and its contents
- **2.Pre-requisites:** Lists and describes the process to install all the required tools, libraries, and environment packages before you can download and install LazyVim
- **3.Install `LazyVim`:** The detailed installation process once ready with all the pre-requisites
- **4.Configure `LazyVim`:** The most challenging part where we go over all the required code and command scripts to be created and added to your corresponding configuration directories
- 5.**Use `LazyVim`:** Cheat sheets, general instructions, specific instructions... You name it, it's in the section. Remember, it's hard to get used to vim, but once you do, there's no going back. VIM, Nvim, and LazyVim, all different faces to the same coin. Vim and NVim are particularly difficult to install, configure, and use. That's where LVIM can into play. It offers a streamlined installation and user-experience. All three IDEs share the same infrastructure and have wide support communities online. In this section, we will reference the most important resources for your reference and to help you kick-off your LVIM journey!
- 6.**Vim_Configuration_Template**: Our setup and configuration template.

## Pre-requisites

### Step One

The first step is to download a proper terminal Emulator. Here are the shortlisted options from best to worse:

| Terminal Emulator | Download                                        | Install                         | Pros                                                                                                |
| ----------------- | ----------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------- |
| Alacritty         | [alacrity.org](https://alacritty.org)           | `brew install --cask alacritty` | By far the lightest, most efficient, and most reliable. Has all the functionalities.                |
| iTerm2            | [iterm2.com](https://iterm2.com/downloads.html) | brew install --cask iterm2      | Second best after alacritty.                                                                        |
| Tabby             | [tabby.sh](https://tabby.sh)                    | brew install --cask tabby       | Nothing special, 3rd best option.                                                                   |
| Warp              | [warp.dev](https://www.warp.dev)                | brew install --cask warp        | Very advanced and usefull for everything except VIM. Excellent choice for normal terminal usecases. |

### Step Two

The terminal must be configured as follows for the full VIM experience:

- Go to `~/.config/alacritty/` (or whichever terminal you choose), you should see an `alacritty.yml` file
- If you can't find the `yml` file or the folder, create them as follows: `mkdir ~/.config/alacritty`; `touch alacritty.yml`
- Once the above steps are complete, proceed to the next step. We will circle back to the `alacritty.yml` file once `LazyVim` is installed.

### Step Three

Make a copy of the alacrity file template below and paste the contents into your `alacritty.yml` file (Note: You might need to have `nvim` installed first if you don't how to use the available terminal text editors. Alternatively, research available native terminal text editors.)

```yaml
# Comprehensive Configuration for Alacritty on M1 MacBook Pro

# Environment Variables
env:
  TERM: xterm-256color

# Window Configuration
window:
  dimensions:
    columns: 100
    lines: 100
  position:
    x: 0
    y: 0
  padding:
    x: 6
    y: 6
  dynamic_padding: false
  decorations: full
  startup_mode: "Windowed"
  title: "Alacritty"

# Scrolling Configuration
scrolling:
  history: 5000
  multiplier: 3
  autoscroll: false

# Tab Configuration
tabspaces: 8

# Font Configuration
font:
  normal:
    family: "YOUR-SELECTED Nerd Font"
  bold:
    family: "YOUR-SELECTED Nerd Font"
  italic:
    family: "YOUR-SELECTED Nerd Font"
  bold_italic:
    family: "YOUR-SELECTED Nerd Font"
  size: 15.75
  offset:
    x: 1
    y: 1
  glyph_offset:
    x: 0
    y: 0
  draw_bold_text_with_bright_colors: true

# Key Bindings
key_bindings:
  - { key: V, mods: Command, action: Paste }
  - { key: C, mods: Command, action: Copy }
  - { key: W, mods: Command, action: Quit }

# Shell Configuration
shell:
  program: /bin/zsh
  args:
    - --login
```

### Step Four

follow the steps in the macOS configuration document to download, install, and reference the correct `NerdFonts` in your alacritty.yml files

- Note that this is important for the icons, symbols, text rendering, etc...

### Step Five

These are the required libraries to download and install for LazyVim to work, we will cover the full environment requirements along with all the details in the Env section in the 'MacEnv.md' configuration file:

- Python
- Npm
- Java

## 3.Install `LazyVim`

Now that we've completed the MacOS and Environment configurations (MacEnv.md) as well as the pre-requisites section above, we may proceed to installing LazyVim:

Easy installation

brew install --cask lazy

OR

You can skip the first step if you haven't install VIM before:

- Step_1 Make a backup of your current Neovim/vim files:

```"
# required
mv ~/.config/nvim{,.bak}

# optional by recommended
mv ~/.local/share/nvim{,.bak}
mv ~/.local/state/nvim{,.bak}
mv ~/.cache/nvim{,.bak}
```

- Step_2 Clone the starter:

```"
git clone https://github.com/LazyVim/Starter ~/.config/nvim
```

- Step_3 Remove the .git folder, so you can add it to your own repo later:

```"
rm -rf ~/.config/nvim/.git
```

- Step_4: If you face issues with the installation, run the following command to remove the directory all together:

```"
rm -rf ~/.config/nvim/.git
```

- Step_5 Start Nvim by simply typing `nvim` in your installed terminal:

```"
nvim
```

By now, you should have been able to successfully install and access vim. If you're facing any troubles, refer to the below listed website for the latest instructions. If all fails, reach out to the Roy Hleis.

[LazyVim](https://www.lazyvim.org/installation)

## 4.Configure_LazyVim

LazyVim is open on your machine, it's already running it's installers settings and updates.
Before you can get to work, there are still a few boxes to check to get everything right:
The list of all installed plugins, LSPs, and extras in under the last section `Vim Configuration Details`
First Things First:

- **Step_1** Press "l" (lower case L) on your keyboard while on LazyVim's home:
  ![Vim_Home](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Home_and_Plugins/Vim_home.jpg)
- **Step_2** once you press on l, the lazy plugin manager will open as follows:
  ![Vim_PluginManager](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Home_and_Plugins/Plugin_Manager.jpg)
- **Step_3** Turn on capslock and press the following keyboard keys in sequence: D, C, U, I(choose the plugins that you want or must install, click "i" for each plugin you want to install), U, and finally S. The below screenshots show how pressing on the mentioned keyboard keys actually moves between tabs. Note that capslock letters are reserved for tabs, and lowercase letters are resever for actions (I = go to installation menu, i = install package):
  ![Vim_Plugin_Install](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Home_and_Plugins/Install.jpg)
  ![Vim_Clean](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Home_and_Plugins/Clean.jpg)
  ![Vim_Sync](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Home_and_Plugins/Sync.jpg)
- **Step_4** press ":" followed by "q" and lastly hit "Enter". This will close Nvim
- **Step_5** type "exit" in alacritty (or the terminal you're using) to exit terminal completely
- **Step_6** Re-open terminal again
- **Step_7** Navigate to the correct directory as follows:

```"
cd home/users/yourUserName/ProperDirectory
```

- **Step_8** Launch nvim by typing nvim in your terminal after you successfully navigate to the correct directory
- **Step_9** While on Vim's home screen (First screenshot from the above batch), press lowerc "x" to access the extras

  - Similar to what you've done for the plugins part,
  - refer to the last section of this document to identify the required extras,
  - Instead of lowercase "i", in this plugin manager, you must use "x" to install/uninstall (or enable/disable) extras
  - Enable all the ones that are listed in this document below,
  - Proceed to next step

  ![Extras](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Extras/Extras.jpg)

- **Step_10** Restart nvim (steps 4 through 8)
- **Step_11** While on the homescreen, click on C and check out the configuration files

  - Remember how to access the config files as you will have to access them every now and then
  - The same feature used to explore and preview the config files can be accessed by pressing "Space" twice anywhere in vim while in "Normal Mode"
  - Most of these files are obsuscated as we're downloading this version of Lvim from an already customized/off-the-shelf repository

  ![Vim_Config_and_Preview](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Config_Files/Configuration_and_Preview.jpg)

- **Step_12** while in normal mode, press "Space" followed by the lowercase letters "c" and "m"
- **Step_13** This will open the mason.nvim for LSP management. In this section, you choose and download the language server providers that you need for your roles/responsibilities

  - Install everything in the provided template at the end of this document

    ![Vim_Mason_LSP](/Users/roy/Directories/uberPosition/TimeMachine/screenshots/vim/Installed_Plugins_LSPs/MasonLSP1.jpg)

- **Step_14** Restart nvim (steps 4 --> 8)
- **Step_15** Check that everything is working as expected
- **Last_Step** when all the above is done and installed. You may proceed to the next step of the initial configuration:

  - This is required for the markdown automatic formatter to stop generating the line-length error which is set to 80 character-limit by default
  - Create a new `.json` file as follows: .markdownlint.jsonNote
  - Note that the "." in the beggining hides the file automatically. It's a must for nvim
  - Press "Shift"+"H" (capslock H) while in the directory tree in order to unhide all hidden files (Just in case you're wondering where the file went after you created it.

    ```JSON
    {
    "MD013": { "line_length": 1400 }
    }
    ```
