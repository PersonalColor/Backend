import express from 'express'
import envConfig from './config/env'

async function main() {
  const PORT = envConfig.PORT ?? 4000

  const server = express()

  server.listen(PORT, () => {
    console.log(`Start PICode server - 0.0.0.0:${PORT}`)
  })
}

main()

process.on('SIGINT', () => {
  console.log(`Quit Sever`)
  process.exit()
})
