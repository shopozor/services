const express = require('express')
const router = express.Router()

// This route is only maintained for k8s monitoring purposes
router.get('/', function (req, res, next) {
  res.status(200)
})

module.exports = router
