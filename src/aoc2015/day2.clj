(ns aoc2015.day2
  (:require [clojure.string :as str]))

(defn wrapping-paper
  [w l h]
  (let [sides [(* w l) (* l h) (* w h)]
        min-side (apply min sides)]
    (+ (apply + (map #(* % 2) sides)) min-side)
    )
  )

(defn part1
  [input]
  (let [lines (str/split input #"\n")
        dimensions (map #(map read-string (str/split % #"x")) lines)]
    (apply + (map #(apply wrapping-paper %) dimensions))
    )
  )

(defn smallest-perimeter
  [w l h]
  (let [sides [(+ w l) (+ l h) (+ w h)]
        sides (map #(* 2 %) sides)
        min-side (apply min sides)]
    min-side
    )
  )

(defn part2
  [input]
  (let [lines (str/split input #"\n")
        dimensions (map #(map read-string (str/split % #"x")) lines)]
    (apply + (map #(+ (apply smallest-perimeter %) (apply * %)) dimensions))
    )
  )