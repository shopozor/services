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

  return child
}

module.exports = {
  generate
}
