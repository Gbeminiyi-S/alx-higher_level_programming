# 0x14. JavaScript - Web scraping

An introductory project on:
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and fetch API
- How to read and write a file using `fs` module

## Requirements
- Files are interpreted on Ubuntu 14.04 LTS using `node` (version 14.x)
- First line of all your files should be exactly `#!/usr/bin/node`
- Code should be semistandard compliant (version 16.x.x)
- Files must be executable
- Not allowed to use `var`

## File Descriptions
### Mandatory
[0-readme.js](./0-readme.js) - a script that reads and prints the content of a file

Requirements
- The first argument is the file path
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object
```
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!

guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
guillaume@ubuntu:~/0x14$
```

[1-writeme.js](./1-writeme.js) - a script that writes a string to a file

Requirements
- The first argument is the file path
- The second argument is the string to write
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object
```
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$ 
```

[2-statuscode.js](./2-statuscode.js) - a script that display the status code of a GET request

Requirements

- The first argument is the file path
- The status code must be printed like this: `code: <status code>`
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
guillaume@ubuntu:~/0x14$ 
```

[3-starwars_title.js](./3-starwars_title.js) - a script that prints the title of a Star Wars movie where the episode number matches a given integer

Requirements

- The first argument is the movie ID
- Use the [Star wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
guillaume@ubuntu:~/0x14$ 
```

[4-starwars_count.js](./4-starwars_count.js) - a script that prints the number of movies where the character “Wedge Antilles” is present

Requirements

- The first argument is the API URL of the [Star wars API](https://swapi-api.alx-tools.com/): `https://swapi-api.alx-tools.com/api/films/`
- Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
guillaume@ubuntu:~/0x14$ 
```

[5-request_store.js](./5-request_store.js) - a script that gets the contents of a webpage and stores it in a file

Requirements

- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be UTF-8 encoded
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>

guillaume@ubuntu:~/0x14$ 
```

[6-completed_tasks.js](./6-completed_tasks.js) - a script that computes the number of tasks completed by user id

Requirements

- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
- Only print users with completed task
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
guillaume@ubuntu:~/0x14$
```

[100-starwars_characters.js](./100-starwars_characters.js)- a script that prints all characters of a Star Wars movie:

Requirements

- The first argument is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name by line
- Must use the [Star wars API](https://swapi-api.alx-tools.com/)
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
guillaume@ubuntu:~/0x14$ 
```

[101-starwars_characters.js](./101-starwars_characters.js)- a script that prints all characters of a Star Wars movie:

Requirements

- The first argument is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name by line __in the same order of the list “characters” in the /films/ response__
- Must use the [Star wars API](https://swapi-api.alx-tools.com/)
- Must use the module `request`
```
guillaume@ubuntu:~/0x14$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
guillaume@ubuntu:~/0x14$ 
```
