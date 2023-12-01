function database(var1, var2) {
    var mysql = require('mysql');

    var con = mysql.createConnection({
    host: "gz-cynosdbmysql-grp-6ml1wj8z.sql.tencentcdb.com", // 远程数据库服务器的IP地址
    port: 27898, // 远程数据库端口，如果是默认端口可以省略
    user: "root", // 数据库用户名
    password: "652398Aq", // 数据库密码
    database: "project" // 要连接的数据库名
    });

    con.connect(function(err) {
    if (err) {
        console.error('Error connecting: ' + err.stack);
        return;
    }

    console.log('Connected as id ' + con.threadId);
    });

    var sql_query = "INSERT INTO table_user VALUES (${var1}, ${var2});";
    con.query(sql_query, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
    });

    module.exports = {inserData};

    con.end();
}

export default database;