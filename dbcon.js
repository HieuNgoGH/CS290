var mysql = require('mysql');
var pool = mysql.createPool({
  connectionLimit : 10,
  host            : 'mysql.eecs.oregonstate.edu',
  user            : 'cs290_ngoh',
  password        : '4584',
  database        : 'cs290_ngoh'
});

module.exports.pool = pool;
