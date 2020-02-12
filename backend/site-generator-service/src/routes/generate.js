const express = require('express')
const router = express.Router()
const generator = require('../generator')

router.get('/', function (req, res, next) {
  res.status(200)
    .send('Generate!')
  // TODO: deal here with the child process (e.g. kill it if necessary)!
  generator.generate()
})

module.exports = router
