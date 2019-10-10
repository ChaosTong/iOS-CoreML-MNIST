//
//  ViewController.swift
//  iOS-CoreML-MNIST
//
//  Created by Sri Raghu Malireddi on 02/08/18.
//  Copyright © 2018 Sri Raghu Malireddi. All rights reserved.
//

import UIKit
import CoreML

class ViewController: UIViewController {

    @IBOutlet weak var drawView: DrawView!
    @IBOutlet weak var predictLabel: UILabel!
    let forestModel = mnistForest()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        predictLabel.isHidden = true
    }

    @IBAction func tappedClear(_ sender: Any) {
        drawView.lines = []
        drawView.setNeedsDisplay()
        predictLabel.isHidden = true
    }
    
    @IBAction func tappedDetect(_ sender: Any) {
        // Fancy Image conversions
        let viewContext = drawView.getViewContext()
        
        let output = try? forestModel.prediction(image: preprocess(cgcontext: viewContext!, width: 28, height: 28)!)
        // Output
        predictLabel.text = output?.output
        predictLabel.isHidden = false
        print(output!.classProbability)
    }
    
    // MARK: - 转MLMultiArray, RGB颜色转灰度值, 和训练model结果偏差原因: 灰度值算法与训练数据的算法不统一导致
    func preprocess(cgcontext: CGContext, width: Int, height: Int) -> MLMultiArray? {
        let cgImage = cgcontext.makeImage()!
        let pd = pixelData(cgImage: cgImage, width: width, height: height)!
        let pixels = pd.map({ Double($0) })
        guard let array = try? MLMultiArray(shape: [height, width] as [NSNumber], dataType: .double) else {
            return nil
        }
        // 取 R G B 数组, A丢弃
        let r = pixels.enumerated().filter { $0.offset % 4 == 0 }.map { $0.element }
        let g = pixels.enumerated().filter { $0.offset % 4 == 1 }.map { $0.element }
        let b = pixels.enumerated().filter { $0.offset % 4 == 2 }.map { $0.element }

        // https://developer.apple.com/documentation/accelerate/vimage/converting_color_images_to_grayscale
        for (index, _) in r.enumerated() {
            let gray = Int((r[index]*0.2126 + g[index]*0.7152 + b[index]*0.0722))
            print(gray)
            array[index] = NSNumber(value: gray)
        }

        return array
    }
    
    // MARK: - 图片转RGBA数组
    func pixelData(cgImage: CGImage, width: Int, height: Int) -> [UInt8]? {
        let size = CGSize(width: width, height: height)
        let dataSize = size.width * size.height * 4
        var pixelData = [UInt8](repeating: 0, count: Int(dataSize))
        let colorSpace = CGColorSpaceCreateDeviceRGB()
        let context = CGContext(data: &pixelData,
                                width: Int(size.width),
                                height: Int(size.height),
                                bitsPerComponent: 8,
                                bytesPerRow: 4 * Int(size.width),
                                space: colorSpace,
                                bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)
        context?.draw(cgImage, in: CGRect(x: 0, y: 0, width: size.width, height: size.height))

        return pixelData
    }
    
}
