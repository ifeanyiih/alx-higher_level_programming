#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const taskobj = {};
request(url, function (error, response, body) {
  if (error) console.log(error);
  const todos = JSON.parse(body);
  for (const todo of todos) {
    if (!Object.keys(taskobj).includes(String(todo.userId))) {
      let count = 0;
      if (todo.completed) count += 1;
      taskobj[todo.userId] = count;
    } else {
      if (todo.completed) taskobj[todo.userId]++;
    }
  }
  for (const key of Object.keys(taskobj)) {
    if (taskobj[key] === 0) delete taskobj[key];
  }
  console.log(taskobj);
});
