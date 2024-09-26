## How to Use

1. Rename 'sources.list':

```bash
sudo mv /etc/apt/sources.list /etc/apt/sources.offical
```

1. **Store Different Mirrors**:

   - You can store different mirror configurations in files named `/etc/apt/sources.offical.<something>`, where `<something>` is a descriptive name for the mirror. For example:
     - `/etc/apt/sources.offical.us`
     - `/etc/apt/sources.offical.eu`
     - `/etc/apt/sources.offical.asia`

2. **Create a Symbolic Link for `mirror.py`**:

   - To make `mirror.py` executable from anywhere, you can create a symbolic link to it in a directory that is included in your `PATH`. A common choice is `/usr/local/bin`.
   - First, ensure that `mirror.py` has executable permissions:

     ```bash
     chmod +x /path/to/mirror.py
     ```

   - Then, create the symbolic link:

     ```bash
     sudo ln -s /path/to/mirror.py /usr/local/bin/mirr
     ```

   - Verify the symbolic link:

     ```bash
     ls -l /usr/local/bin/mirror
     ```

     The output should look like this:

     ```bash
     lrwxrwxrwx 1 root root 21 Sep 26 20:05 /usr/local/bin/mirror -> /path/to/mirror.py
     ```

3. **Test the Script**:

   - You can now run the `mirror` command from anywhere to execute `mirror.py`:

     ```bash
     sudo mirr
     ```
