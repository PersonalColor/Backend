import DataProductManager from '../module/data/product/productManager'
import DataStyleManager from '../module/data/style/styleManager'

export default class IntervalManager {
  static run() {
    DataProductManager.run()
    DataStyleManager.run()
  }
}
