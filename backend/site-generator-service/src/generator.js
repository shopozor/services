const { spawn } = require('child_process')

function generate () {
  const child = spawn('yarn', ['generate'], {
    cwd: process.env.SRC_DIR || '/data/frontend/consumer-ui',
    shell: true
  })

  child.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`)
  })

  child.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`)
  })

  child.on('close', (code) => {
    console.log(`child process exited with code ${code}`)
  })

  child.on('error', (err) => {
    console.log(`Error: ${err}`)
  })

  return child
}

module.exports = {
  generate
}
