import { spawn } from 'child_process'
import { DataDirectoryPath } from '../../../types/module/data/data.types'

export default class DataProductManager {
  static getProductPath() {
    return `${DataDirectoryPath}/product`
  }

  static getProductList() {
    
  }

  static updateProductData() {
    const result = spawn('./src/scripts/venv/Scripts/python', ['./src/scripts/scanConfig.py', ''])

    result.stdout.on('data', function (data) {
      if (data === undefined) return
      console.log(JSON.parse(data))
    })
  }

  static async run() {
    setInterval(() => {
      this.updateProductData()
    }, 60 * 60 * 6 * 1000)
  }

  static create() {

  }

  static delete() {
    
  }
}
