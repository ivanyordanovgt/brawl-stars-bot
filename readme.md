# Tutorial 
### The version in this repo is outdated. The download has been moved to the discord group
Account details:<br>
username: pylarelease <br>
password: pylareleasehooray <br>

Youtube tutorial: [vid](https://www.youtube.com/watch?v=eXtHx8-gJ3g)


1. Create a github account and star the repo
2. Join the discord:
[discord](https://discord.gg/dVUeqYERVz)
3. Follow the tutorial in the #download-guide channel
   
# How to make the bot play the best
Play 3v3 on brawl ball with brawlers that can auto aim easily! Nita / Jacky / Doug etc have the best results.

# Can you get banned?
Most likely no. There are similiar bots out there that are way more blatantly playing like a bot and are fine. There's always a small risk tho.

# PC detects it's a virus?

## Short explanation:

1. Python code is converted into exe without an license, antivirus instantly finds the file suspicous 
2. The tool I use to convert into exe is very secure and hard to decompile so people who make viruses also use it so their viruses cannot be decompiled / removed etc.
However, even tho the tool makes the code not possible to decompile it has a patterns of doing these things, which the antiviruses have an dataset for. Once the antivirus sees the pattern it instantly
flags it as every possible trojan/worm etc etc.

## Long explanation

When analyzing the root causes behind false positive detections of executables compiled from Python code, it's crucial to delve deeper into the intricacies of both the compilation process and the mechanisms employed by antivirus software.

Heuristic analysis, a cornerstone of modern antivirus solutions, involves the dynamic examination of file behavior and code structures to identify potential threats. This method relies on a set of predefined rules and algorithms to recognize patterns indicative of malicious intent. In the case of Python code compiled into executables, heuristic analysis may raise red flags if the behavior of the resulting binary resembles that of known malware. For instance, if the executable initiates unauthorized network connections, attempts to modify critical system files, or exhibits other suspicious activities, it may trigger heuristic warnings, despite being a legitimate application.

Moreover, the compilation process itself introduces complexities that can contribute to false positive detections. Compilers and packaging tools often employ techniques like code obfuscation and packing to optimize performance, reduce file size, or safeguard intellectual property. However, these optimization methods can inadvertently mirror the tactics employed by malware authors to evade detection. The obfuscated or packed code might exhibit characteristics that resemble those of malicious software, such as encrypted payloads, polymorphic code patterns, or evasive runtime behaviors. As a result, antivirus algorithms may interpret these traits as indicators of a potential threat, leading to false positives.

Furthermore, the existence of shared signatures within antivirus databases exacerbates the issue of false positives. If a particular compilation tool and configuration have been associated with the creation of malware in the past, antivirus vendors may include the corresponding signatures in their threat intelligence databases. Consequently, any executable produced using similar compilation settings or methodologies may trigger false positive detections due to the shared signature with known malicious code. This scenario highlights the challenges of distinguishing between benign and malicious software, particularly when certain tools or techniques have been exploited by both legitimate developers and cybercriminals alike.

In summary, false positive detections of executables compiled from Python code stem from a combination of heuristic analysis limitations, complexities inherent in the compilation process, and the presence of shared signatures within antivirus databases. While these detections can be disruptive and concerning for developers and users alike, they underscore the ongoing need for refined detection algorithms, transparent communication between antivirus vendors and software developers, and user education regarding the nuances of cybersecurity threats and defense mechanisms.
