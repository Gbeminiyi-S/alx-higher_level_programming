#!/usr/bin/node
// Display the status code of a GET request

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
    console.log(`code: ${response.statusCode}`);
});
