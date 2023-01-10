(ns aoc2015.day1
  (:require [clojure.string :as str]))

(defn goto
  [start floor-diffs]
  (reduce (fn [acc v] (+ acc v)) start floor-diffs)
  )

(defn parse-floor-diffs
  [floor-text]
  (map #(condp = % "(" 1 ")" -1) (str/split floor-text #""))
  )

(defn part1
  [input]
  (goto 0 (parse-floor-diffs input))
  )

(defn find-position
  [floor-diffs]
  (loop [floors floor-diffs
         current 0
         position 0]
    (cond
      (= current -1) position
      (empty? floors) -1
      :else (recur (rest floors) (+ (first floors) current) (inc position))
      )
    )

  )

(defn part2
  [input]
  (find-position (parse-floor-diffs input))
  )
