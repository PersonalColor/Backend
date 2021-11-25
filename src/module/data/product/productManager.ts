import { spawn } from 'child_process'
import { DataDirectoryPath } from '../../../types/module/data/data.types'
import { existsSync, mkdirSync, writeFileSync, readFileSync } from 'fs'

export default class DataProductManager {
  static getProductPath() {
    const defaultPath = `${DataDirectoryPath}/product`

    if (!existsSync(defaultPath)) {
      mkdirSync(defaultPath, { recursive: true })
    }

    return defaultPath
  }

  static getProductList() {
    return JSON.parse(readFileSync(`${this.getProductPath()}/product.json`).toString())
  }

  static updateProductData() {
    const result = spawn('./src/scripts/venv/Scripts/python', ['./src/scripts/coupang_search_crawling.py'])

    result.stdout.on('data', function (data) {
      writeFileSync('./data/product/product.json', data)
    })

    result.stderr.on('data', function (data) {
      console.log(data.toString())
    })
  }

  static async run() {
    this.updateProductData()
    setInterval(() => {
      this.updateProductData()
    }, 60 * 60 * 6 * 1000)
  }

  static create() {}

  static delete() {}
}
