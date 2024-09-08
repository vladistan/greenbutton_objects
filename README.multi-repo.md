# How to use multi-repo dev container setup

1. Make sure you have forks of both greenbutton and home-energy-analysis-tool in your github account.
   - [Fork greenbutton](https://github.com/codeforboston/greenbutton_objects/fork)
   - [Fork home-energy-analysis-tool](https://github.com/codeforboston/home-energy-analysis-tool/fork)


2. Make sure multi-repo branch is in your forked repo. Do this on your local machine.
   Make sure to replace `YOUR_GITHUB_USERNAME` with your actual github username.

```
  GITHUB_USERNAME=YOUR_GITHUB_USERNAME
  mkdir multi-repo
  cd multi-repo

  git clone "git@github.com:${GITHUB_USERNAME}/greenbutton_objects.git"
  cd greenbutton_objects
  git remote add vlad "https://github.com/vladistan/greenbutton_objects.git"
  git fetch --all
  git checkout multi-repo-container
  git push origin multi-repo-container
  cd ..

  git clone git@github.com:${GITHUB_USERNAME}/home-energy-analysis-tool.git
  cd home-energy-analysis-tool
  git remote add vlad "https://github.com/vladistan/home-energy-analysis-tool.git"
  git fetch --all
  git checkout multi-repo-container
  git push origin multi-repo-container
  cd ..

  cd ..
```


3. Start Github codespace with options make sure to select correct branch `multi-repo-container` and correct configuration 'With Home Energy App' as shown below:

<img src="images/codespace-multi-repo.png" width="500px" />

4. Once the codespace starts up and you see a message like the one below, wait for the setup to complete.

```
Finishing up
Running postStartCommand
.devcontainer/post_start.sh
```

5. Once your setup completes and you see that your VSCode extensions button in the toolbar looks like the one below click on it to see if any you have to do any extra actions like reloading a window before you can start working on the code

   ![Extensions loading](images/vscode_extension_attention_needed.png)
   ![Extensions wait](images/vscode_extension_wait.png)
