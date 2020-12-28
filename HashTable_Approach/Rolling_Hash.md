# Rolling Hash:

> > Rolling hashes are amazing, they provide you an ability to calculate the hash values without rehashing the whole string. 
> > In a nutshell, a rolling hash is to a normal hash as a moving average is to a simple average, 
> > i.e. it's calculated on items within a "window" that moves across the full range of your data.
> > Rolling hash functions are generally designed such that, when you move the data "window", 
> > calculating the new hash does not involve a complete recalculation across the entire "window".

Consider this example. Lets say you have a string "abcdeacdoe" & you want to find pattern "bcd" in this string.

Now with naive way, you will try to compare each character of pattern ("bcd") with the string characters ("abcdbbca") forming three character strings. This might be really inefficient specially as the input gets larger. If you use rolling hash, you can do this intelligently.

First you calculate the hash of first three letter substring (abc) in string. To keep matters simple, lets say we use base 7 for this calculation (in actual scenario we should mod it with a prime to avoid overflow):

```
substring1 = a*7^0+ b*7^1+c*7^2=97*1+98*7+99*49=5634
pattern = b*7^0+ c*7^1+d*7^2=98*1+99*7+100*49=5691
```

So you compare two hash values and since they are different, you move forward. 
Now you reach to second substring "bcd" in string. Here is where the fun begins. 
We can calculate the hash of this string without rehashing everything. 
As you can see, the window has moved forward only by dropping one character and adding another:

```
a<- bc<-d
```

Below diagrams explains it better (though it's working on a four letter string rather than three):

![Rolling_Hash_1](https://qph.fs.quoracdn.net/main-qimg-89e257112133ef1f4ab24043afb743c2.webp)

From hash value we drop the first character value, divide the left out value with the base number 
and add the new char to the rightmost position with appropriate power of base: Here are the steps:

> **drop a** => `(a*7^0+ b*7^1+c*7^2) - a*7^0`
>
> **divide everything by 7** => `(b*7^1+c*7^2)/7 => b*7^0 + c*7^1`
>
> **add d** => `b*7^0 + c*7^1 + d*7^2` [the power of base for d is (pattern-length-1)]

Thus new hash for "bcd" in input string would be => `(5634 - 97)/7+ 100*49 = 5691` which matches pattern hash value. 
Now we can go ahead and compare the strings to verify if they are in fact same.

Visualize doing this for a large string which is comprising of, lets say, 30 lines. 
You will be able to get new hash value in constant time without much effort by just dropping and adding new character(s).

In real use cases, to avoid overflow because of large power, we will have to do modulo with large prime. 
This technique is often used for multi-pattern string search and forms the core of algorithm like Karp-Rabin algorithm. 
This algorithm is an excellent choice to detect plagiarism

## Applications:

* **Data Compression:** Rolling Hashing is extremely useful in data compression. 
  In the LZ family of compressors you aim to replace a string that 
  previously occurred by an offset to the previous position and a length, 
  codified in several different forms. If you use a rolling hash and store 
  the results and offsets you don't need to scan all your "memory" 
  to detect repetitions and you can pick a repetition that occurred many thousands of bytes 
  ago without the penalty of looking back.
  
  Imagine a large file concatenated with itself, you should compress 
  it at least in half but most LZ algorithms have a limited window 
  to look for repetitions so they fail to look for this. 
  The **Bentley-McIlroy algorithm** uses a rolling hash to detect exactly this kind of repetitions. 
  It's very useful in systems that do versioning including noSql databases. 
  So while the **Rabin-Karp search** is the classic example there are other 
  interesting applications to a rolling hash that are interesting today.

* **Substring Searching:** For example the 
  [Rabin-Karp string search algorithm](http://en.wikipedia.org/wiki/Rolling_hash#Rabin-Karp_rolling_hash).

#### **Classic problems that can be solved using this technique:**

1. [LeetCode - Problem 187 - Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/)	
1. [LeetCode - Problem 1147 - Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition)	
1. [LeetCode - Problem 1316 - Distinct Echo Substrings](https://leetcode.com/problems/distinct-echo-substrings)	
1. [LeetCode - Problem 1638 - Count Substrings That Differ by One Character](https://leetcode.com/problems/count-substrings-that-differ-by-one-character)	
1. [LeetCode - Problem 1698 - Number of Distinct Substrings in a String](https://leetcode.com/problems/number-of-distinct-substrings-in-a-string)	
