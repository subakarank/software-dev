1. Navigate to your local repository directory using a terminal or command prompt.
2. Use the `git remote -v` command to view the current remote URLs.

    ```bash
    git remote -v
    ```

3. You should see something like this:

    ```
    origin  https://github.com/old_username/old_repository.git (fetch)
    origin  https://github.com/old_username/old_repository.git (push)
    ```

4. To update the remote URL, you'll use the `git remote set-url` command. Replace `old_url` with the old URL and `new_url` with the new URL provided in the message.

    ```bash
    git remote set-url origin new_url
    ```

5. After running the command, you can verify that the URL has been updated by using `git remote -v` again.

    ```bash
    git remote -v
    ```

6. You should now see the updated URL:

    ```
    origin  https://github.com/new_username/new_repository.git (fetch)
    origin  https://github.com/new_username/new_repository.git (push)
    ```

7. Now you can pull or push changes as usual with the updated remote URL.

Keep in mind that you need appropriate permissions to access the new repository location if it belongs to an organization or another user.
