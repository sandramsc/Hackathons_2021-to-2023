const mongoose = require("mongoose");

const UserSchema = mongoose.Schema({
  username: {
    type: String,
    required: true
  },
  email: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  },
  createdAt: {
    type: Date,
    default: Date.now()
  },
  mentor: {
    type: String,
    default: "Jane Jackson"
  },
  jobTitle:{
    type:String,
    required:true
  },
  department:{
    type:String,
    required:true
  }
});

module.exports = mongoose.model("user", UserSchema);
