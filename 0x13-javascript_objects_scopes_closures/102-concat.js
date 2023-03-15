#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const argv = process.argv.slice(2);

if (argv[0] !== undefined) {
  for (const path of argv) {
    fs.stat(path, function (error, stats) {
      if (error) console.log(error);
      // 'r' specifies read mode
      fs.open(path, 'r', (error, fd) => {
        if (error) console.log(error);
        const buffer = Buffer.alloc(stats.size);
        fs.read(fd, buffer, 0, buffer.length,
          null, (error, bytesRead, buffer) => {
            if (error) console.log(error);
            const data = buffer.toString('utf8');
            console.log(data);
          });
      });
    });
  }
}
