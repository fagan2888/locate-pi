
# locate-pi

Seamlessly SSH to a Raspberry Pi at home, or any other server
without a static IP or DNS. Your pi periodically saves its IP address
to a remote, static host, so you always know where it is.

## Setup

1. Set the environment variable `IP_DEST`, which should be a valid
destination for SCP, e.g., add the following to your `~/.bashrc`:

```
export IP_DEST='user@host:/path'
```

2. Authorize the pi's public key at the destination host. For example,
on the pi, run

```
$ ssh-copy-id user@host
```

3. Set a `cronjob` on the pi to sync its IP:

```
$ crontab -e
```

and add a line like

```
0 * * * * /home/pi/locate-pi/ip.py
```

4. Use a shell alias on work machines to automatically SSH wherever
your pi may have wandered:

```
alias pi='ssh pi@`scp -q host:/path/ip.txt /dev/stdout | tail -n 1`'
```

