const util = require('util')
const exec = util.promisify(require('child_process').exec)

async function generate () {
  const child = await exec('"yarn" generate', {
    cwd: process.env.SRC_DIR || '/data/frontend/consumer-ui'
  })

  console.log(`stdout: ${child.stdout}`)
  console.error(`stderr: ${child.stderr}`)
  console.log(`pid: ${child.pid}`)
}

module.exports = {
  generate
}
