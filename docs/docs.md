# Content Factory

Usage of javascript to generate the content on the dom.

Current design steps:

Python uses AI + algo to determine content to fetch and render into the DOM.
Python updates input values based on algo.
Python triggers JS algo through button click:

JS algo: make fetch call to get the images
JS will render image
JS will render the text using HTML.
JS sends get request to the content factory server (flask) to take a screenshot.
React Will use React to trigger.

Python calls interaction proxy to take the screenshot and save it to an image in content factory.

Versions:

1. Usage of buttons and inputs to generate. Python is the brain of the intelligence. Javascript is the brian behind the DOM. Html and CSS will do the rendering as needed. Potential usage of React?

2. Look into python rendering html dynamically without having to use inputs.