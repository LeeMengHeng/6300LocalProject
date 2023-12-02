import { io } from "socket.io-client";

const socket = io("10.12.2.58");

// send a message to the server
socket.emit("GET_ALL_WINDOWS");

// receive a message from the server
socket.on("hello", (arg) => {
    console.log(arg); // prints "world"
});