# ObsidianMermaidJS-AddCodeSnippets
Obsidian supports mermaid js, which can easily create diagrams. However, code snippets cannot be added to diagrams without proper escaping. This python script makes escaping special characters easy.
<img width="850" height="704" alt="image" src="https://github.com/user-attachments/assets/1395e95c-dc93-41e5-a6a9-8629984904b7" />

## Usage
```bash
$ python3 mermaidEscape.py
Enter the payload: "key":{"foo":"bar"} #Output: &quot;key&quot;&colon;&lcub;&quot;foo&quot;&colon;&quot;bar&quot;&rcub;
```
