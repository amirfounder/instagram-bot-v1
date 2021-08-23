This program will require your full computer and screens :o

It's also interesting that I did not need to pip install mitmdump. It looks like just having it on your computer is good enough :D!

# Summary

Git URL: `git@github.com:amirfounder/program-1.git` (Private. Request access if need to pull)

# File Structure

```

|-- 1
  |-- src
    |-- <sub_program>
      |-- <sub_classes>
        |-- ...
      |-- <main_class>.py
      |-- index.py
      ...
    ...
  |-- tests
  |-- .gitignore
  |-- main.py
  |-- readme.md
  |-- requirements.txt
  
```

# Coding Standards

## Runners

- Runner classes act as controllers. There is none / minimal logic in them. The follwoing classes are considers "runners":
  - ProgramRunner
  - [PROJECT_NAME]Runner (i.e `ContentFactoryRunner.py`)
- Runners will typically have a `run()` method with the @classmethod annotation

## High level program logic

- High level program / decision Logic is implemented into the main classes of each project
  - Project directory: `.\src\content_factory\`
  - Project main class: `.\src\content_factory\ContentFactory.py`
  - Project main class will aggregate sub / specialized classes and calls their functions to perform specifics.

## Low level program logic

- Low level logic is implemented into the sub / specialized classes of the project

# Next Steps

NOTE: This section is not a roadmap, as much as it is a todo list. To track all items that were finished on this list, look at git commits.

- File parser --> parse multiple files at once to grab content
- Database manager --> store items in db + basic functionality
- File to database manager --> run at the same time with the mitm proxy
- Interaction proxy --> control the mouse, screen, keyboard
- Content factory --> product basic images
- Database manager --> store images
- Researcher managers --> run research using interaction proxy + http proxy + database managers
- Decision makers --> run decisions on the types of content to create, hashtags to use, etc.
- API connectors --> programs that connect to apis to assist interaction proxy and publish content
