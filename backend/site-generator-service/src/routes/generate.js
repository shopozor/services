const express = require('express')
const router = express.Router()
const generator = require('../generator')

router.get('/', function (req, res, next) {
  const child = generator.generate()
  child.on('close', code => {
    if (code !== 0) {
      const msg = `ps process exited with code ${code}`
      console.error(msg)
      res.status(500).send(`Error: ${msg}`)
    }
    res.status(200)
      .send('Website successfully generated!')
  })
  child.on('error', err => {
    const msg = `Error: ${err}`
    console.error(msg)
    res.status(500).send(msg)
  })
})

module.exports = router
