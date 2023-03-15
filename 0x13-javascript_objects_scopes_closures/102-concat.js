#!/usr/bin/node

const fs = require('fs');

const argv = process.argv.slice(2);

fs.open(argv[2], 'a', (err, wfd) => {
  if (err) console.log(err);
  fs.open(argv[0], 'r', (err, fd) => {
    if (err) console.log(err);
    fs.read(fd, (err, bytesRead, buffer) => {
      if (err) console.log(err);
      fs.write(wfd, buffer, (err, written, string) => {
        if (err) console.log(err);
      });
    });
  });

  fs.open(argv[1], 'r', (err, fd) => {
    if (err) console.log(err);
    fs.read(fd, (err, bytesRead, buffer) => {
      if (err) console.log(err);
      fs.write(wfd, buffer, (err, written, string) => {
        if (err) console.log(err);
      });
    });
  });
});
