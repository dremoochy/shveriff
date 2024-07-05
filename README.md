# Shveriff
A simple script made by me out of boredom using hashlib & some other stuff

usage: python3 mdverify.py [-h | --help] [-hm | --hashmode] [-fh | --filemode] [-m [one of the hashlib modes] | --mode [one of the hashlib modes] ] hashOne hashTwo 

# Basic usage

```
python3 shveriff.py fileOne fileTwo
```

Output : 

```
Calculating...
First file hash (using md5) : aab159126176756db4404e2050a93838
Second file hash (using md5) : aab159126176756db4404e2050a93838
Hash values are identical!
```
Notice that the default hashing method is md5.