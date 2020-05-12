#!/usr/bin/node
const request = require('request');

const url = process.argv.slice(2)[0];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todoList = JSON.parse(body);
    const todoComplete = Object();
    todoList.forEach(function (task) {
      if (task.completed) {
        if (!todoComplete[task.userId]) {
          todoComplete[task.userId] = 1;
        } else {
          todoComplete[task.userId] += 1;
        }
      }
    });
    console.log(todoComplete);
  }
});
