#!/usr/bin/node

const fs = require('fs');

const argv = process.argv.slice(2);

if (argv.length === 3) {
  fs.open(argv[2], 'w', (err, wfd) => {
    if (err) console.log(err);

    fs.stat(argv[0], (err, stats) => {
      if (err) console.log(err);

      fs.open(argv[0], 'r', (err, fd) => {
        if (err) console.log(err);

        const buffer = Buffer.alloc(stats.size);
        fs.read(fd, buffer, 0, stats.size, -1, (err, bytesRead, buffer) => {
          if (err) console.log(err);

          fs.write(wfd, buffer.toString('utf-8'), (err, written, string) => {
            if (err) console.log(err);
          });
        });
      });
      fs.close(wfd, (err) => {
        if (err) console.log(err);
      });
    });
  });

  fs.stat(argv[1], (err, stats) => {
    if (err) console.log(err);

    fs.open(argv[1], 'r', (err, fd) => {
      if (err) console.log(err);

      const buffer = Buffer.alloc(stats.size);
      fs.read(fd, buffer, 0, stats.size, -1, (err, bytesRead, buffer) => {
        if (err) console.log(err);

        fs.appendFile(argv[2], buffer.toString('utf-8'), (err) => {
          if (err) console.log(err);
        });
      });
    });
  });
}
